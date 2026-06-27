import { API_BASE_URL, getApiHealth } from "@/lib/api";

export default async function Home() {
  const health = await getApiHealth();

  return (
    <main style={{ maxWidth: "640px", margin: "4rem auto", padding: "0 1rem" }}>
      <h1>Enterprise AI Platform</h1>
      <p>Corporate AI platform for Acme Corporation.</p>

      <section style={{ marginTop: "2rem" }}>
        <h2>API status</h2>
        {health ? (
          <ul>
            <li>Status: {health.status}</li>
            <li>Service: {health.service}</li>
            <li>Environment: {health.environment}</li>
            <li>Version: {health.version}</li>
          </ul>
        ) : (
          <p>API unreachable at {API_BASE_URL}.</p>
        )}
      </section>
    </main>
  );
}
