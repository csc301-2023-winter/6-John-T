import isProd from "./isProd";

class ConsoleWrapper{

    constructor() {
        if (isProd()) {
            this.flag = false;
        }
        else {
            this.flag = true;
        }
    }

    log(params) {
        if (this.flag) {
            console.log(params);
        }
    }

    error(params) {
        if (this.flag) {
            console.error(params);
        }
    }

    warn(params) {
        if (this.flag) {
            console.warn(params);
        }
    }
}

const consoleWrapper = new ConsoleWrapper();
export { consoleWrapper };