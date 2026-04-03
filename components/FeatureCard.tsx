import { ReactNode } from 'react';
import { useRouter } from 'next/router';

interface FeatureCardProps {
  title: string;
  href: string;
  icon: ReactNode;
  iconColor?: string;
  children: ReactNode;
}

export default function FeatureCard({ title, href, icon, iconColor = '#226cff', children }: FeatureCardProps) {
  const { basePath } = useRouter();
  const isExternal = href.startsWith('http') || href.startsWith('mailto:');

  return (
    <a
      href={isExternal ? href : `${basePath}${href}`}
      target={isExternal ? '_blank' : undefined}
      rel={isExternal ? 'noopener noreferrer' : undefined}
      style={{
        display: 'block',
        padding: '1.25rem 1.5rem',
        borderRadius: '1rem',
        border: '1px solid #e5e7eb',
        boxShadow: '0 2px 8px rgba(0,0,0,0.04)',
        background: '#fff',
        textDecoration: 'none',
        color: 'inherit',
        transition: 'box-shadow 0.15s, border-color 0.15s',
      }}
      onMouseEnter={e => {
        (e.currentTarget as HTMLAnchorElement).style.boxShadow = '0 4px 16px rgba(0,0,0,0.1)';
        (e.currentTarget as HTMLAnchorElement).style.borderColor = '#d1d5db';
      }}
      onMouseLeave={e => {
        (e.currentTarget as HTMLAnchorElement).style.boxShadow = '0 2px 8px rgba(0,0,0,0.04)';
        (e.currentTarget as HTMLAnchorElement).style.borderColor = '#e5e7eb';
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '0.5rem' }}>
        <span style={{ color: iconColor, display: 'flex', alignItems: 'center' }}>{icon}</span>
        <span style={{ fontWeight: 600, fontSize: '0.95rem' }}>{title}</span>
      </div>
      <div style={{ fontSize: '0.875rem', color: '#6b7280', lineHeight: 1.5 }}>{children}</div>
    </a>
  );
}
