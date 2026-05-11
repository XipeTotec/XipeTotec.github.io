/// <reference types="vite/client" />

interface ImportMetaEnv {
  /** TideCheck API key (do not commit; set locally and in CI secrets). */
  readonly VITE_TIDE_API_KEY?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
