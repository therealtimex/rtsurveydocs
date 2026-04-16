import React from 'react';
import type { AppProps } from 'next/app';
import Script from 'next/script';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Component {...pageProps} />
      <Script
        src="https://embed-ex-d4a8523f9a.realtimex.ai/embed/realtimex-chat-widget.min.js"
        data-embed-id="3cbc9350-a031-452f-8425-9f64189d7a16"
        data-base-api-url="https://embed-ex-d4a8523f9a.realtimex.ai/api/embed"
        data-assistant-name="Nagen Assistant Agent"
        data-greeting="Send a chat to get started."
        data-button-color="#262626"
        data-user-bg-color="#3DBEF5"
        data-assistant-bg-color="#FFFFFF"
        strategy="afterInteractive"
      />
    </>
  );
}
