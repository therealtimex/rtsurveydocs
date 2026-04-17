import React from 'react';
import type { AppProps } from 'next/app';
import Script from 'next/script';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Component {...pageProps} />
      <Script
        src="https://embed-ex-5e9c7b7337.realtimex.ai/embed/realtimex-chat-widget.min.js"
        data-embed-id="d912063b-1519-4b6b-9e66-ead46ca6aa5e"
        data-base-api-url="https://embed-ex-5e9c7b7337.realtimex.ai/api/embed"
        data-assistant-name="Nagen agent assistent"
        data-greeting="Send a chat to get started."
        data-button-color="#262626"
        data-user-bg-color="#3DBEF5"
        data-assistant-bg-color="#FFFFFF"
        strategy="afterInteractive"
      />
    </>
  );
}
