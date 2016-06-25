# exports

> node foo.js

foo.js에 있는 `var circle = require('./circle.js')`. node가 require를 파싱하고, circle.js에 들어가서 exports 전역 객체에 붙어있는 속성들을 circle 변수에 붙여줍니다.

- https://nodejs.org/api/globals.html#globals_exports
- https://nodejs.org/api/modules.html#modules_modules

# module.exports

> node bar.js

square 자체가 함수가 되었습니다.

- https://nodejs.org/api/globals.html#globals_module

