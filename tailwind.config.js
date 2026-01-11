/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'Sora', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        '2xl': '1rem',
        '4xl': '2rem', // Rounded-[2rem] as requested
      },
      colors: {
        background: '#FFFFFF',
      }
    },
  },
  plugins: [],
}
