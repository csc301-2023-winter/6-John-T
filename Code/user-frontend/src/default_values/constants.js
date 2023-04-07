import isProd from "../utils/isProd";

export const BACKEND_URL = isProd() ? 'https://6-john-t-production-f786.up.railway.app' : 'https://6-john-t-production.up.railway.app';

export const BACKEND_PATH_FOR_BENCH_DETAILS = '/benches/get_user_bench/';