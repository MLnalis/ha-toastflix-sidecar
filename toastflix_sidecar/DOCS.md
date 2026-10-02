# ToastFlix Audio Sidecar

Microservizio che sincronizza e fornisce l'audio italiano per i flussi Dual Audio di ToastFlix.

## Opzioni

- **public_url**: URL pubblico HTTPS (es. `https://nome.tailnet.ts.net`). Il server ToastFlix deve poterlo raggiungere.
- **audio_proxy**: proxy SOCKS5/HTTP usato solo per la Fonte 2 (es. `socks5h://IP:1080` per WARP). Lascia vuoto se non serve.
- **offset_api_url**: API ToastFlix per sincronizzare gli offset acustici.
- **cors_origins**: origini CORS consentite (default `*`).

## Porta

La dashboard e' su `http://IP_DI_HA:3169`.

## Accesso da Internet

Esponi la porta 3169 con Tailscale Funnel (`tailscale funnel 3169`) o con un tunnel Cloudflare,
poi inserisci l'URL HTTPS in `public_url` e nel configuratore ToastFlix (Server audio DUAL).

## Dati

Cache e database offset sono salvati in `/data` e inclusi nei backup di Home Assistant.
