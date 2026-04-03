import { useEffect } from 'react';
import { useRouter } from 'next/router';

export default function NotFound() {
  const router = useRouter();

  useEffect(() => {
    const path = window.location.pathname;
    // Redirect old Hugo /docs/* URLs to new root paths
    if (path.startsWith('/docs/')) {
      const newPath = path.replace(/^\/docs/, '');
      window.location.replace(newPath || '/');
    }
  }, []);

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>404 — Page Not Found</h1>
      <p>
        <a href="/">Go to homepage</a>
      </p>
    </div>
  );
}
