// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  colorMode: {
    preference: "light",
  },
  modules: [
    "@nuxtjs/supabase",
    "@nuxt/image",
    "@nuxt/ui",
    "@nuxtjs/tailwindcss",
  ],
  supabase: {
    redirectOptions: {
      // Pour rediriger l'utilisateur si il n'est pas connecté
      login: "/login", // Redirige vers la page de login s'il nes pas connecté ou s'il s'est logout
      callback: "/",
      exclude: [
        // Page que l'utilisateur peut visiter sans être connecté
        "/login",
        "/register",
        "/",
        "/index",
        "/img/*",
        "/detail/*",
        "/updatePassword",
        "/resetPassword",
      ],
    },
  },
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
    }
  }
});
