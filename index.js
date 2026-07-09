export default {
  async fetch(request, env) {
    const ZONE_ID = env.ZONE_ID;
    const API_TOKEN = env.API_TOKEN;
    const EMAIL = env.CLOUDFLARE_EMAIL;

    if (!ZONE_ID || !API_TOKEN || !EMAIL) {
      return new Response('Missing configuration', { status: 500 });
    }

    const now = new Date();
    const endDate = now.toISOString().split('T')[0];
    const startDate = new Date(now);
    startDate.setDate(startDate.getDate() - 30);
    const startDateStr = startDate.toISOString().split('T')[0];

    const query = `
      query GetAnalytics($zoneTag: string, $start: string, $end: string) {
        viewer {
          zones(filter: {zoneTag: $zoneTag}) {
            httpRequests1dGroups(
              limit: 30,
              filter: {date_gt: $start, date_lt: $end}
            ) {
              dimensions { date }
              sum { requests bytes visits }
            }
          }
        }
      }
    `;

    const variables = { zoneTag: ZONE_ID, start: startDateStr, end: endDateStr };

    try {
      const response = await fetch('https://api.cloudflare.com/client/v4/graphql', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${API_TOKEN}`,
          'X-Auth-Email': EMAIL
        },
        body: JSON.stringify({ query, variables })
      });

      const data = await response.json();

      if (data.errors) {
        return new Response(JSON.stringify({ error: data.errors }), {
          status: 500,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const zoneData = data.data?.viewer?.zones?.[0];
      if (!zoneData || !zoneData.httpRequests1dGroups) {
        return new Response(JSON.stringify({ error: 'No data' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      let totalRequests = 0, totalBytes = 0, totalVisits = 0;
      zoneData.httpRequests1dGroups.forEach(day => {
        totalRequests += day.sum.requests || 0;
        totalBytes += day.sum.bytes || 0;
        totalVisits += day.sum.visits || 0;
      });

      return new Response(JSON.stringify({
        requests: totalRequests,
        bandwidth: totalBytes,
        visits: totalVisits,
        updated: new Date().toISOString()
      }), {
        headers: { 'Content-Type': 'application/json' }
      });

    } catch (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};
