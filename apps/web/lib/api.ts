/**
 * Server-side access to the backend API.
 *
 * These functions run only on the server (in Server Components or route handlers),
 * so the API base URL is a server-only env var — never exposed to the browser. This
 * is the seed of the Backend-for-Frontend (BFF) pattern, fleshed out in Release 2.
 */

export const API_BASE_URL = process.env.API_BASE_URL ?? "http://localhost:8000";

export type ApiHealth = {
  status: string;
  service: string;
  environment: string;
  version: string;
};

export async function getApiHealth(): Promise<ApiHealth | null> {
  try {
    const response = await fetch(`${API_BASE_URL}/health`, { cache: "no-store" });
    if (!response.ok) {
      return null;
    }
    return (await response.json()) as ApiHealth;
  } catch {
    return null;
  }
}
