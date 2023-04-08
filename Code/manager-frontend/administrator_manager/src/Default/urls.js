//taken from user frontend side
import isProd from "./isProd";

export const BACKEND_URL = isProd() ? 'https://6-john-t-production-f786.up.railway.app' : 'https://6-john-t-production.up.railway.app';
//export const BACKEND_URL = 'http://127.0.0.1:8000';