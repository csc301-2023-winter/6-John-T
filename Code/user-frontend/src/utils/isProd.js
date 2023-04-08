// its prod environment if its not being run on netlify site.
export default function isProd() {
  return window.location.hostname.includes('netlify.app');
}