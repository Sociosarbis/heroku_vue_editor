export default function (callback, interval) {
  let lastTime = Date.now();
  let timeoutId = 0;
  return (evt) => {
    if (Date.now() - lastTime >= interval) {
      clearTimeout(timeoutId);
      callback(evt);
      lastTime = Date.now();
      timeoutId = 0;
    } else if (timeoutId === 0) {
      timeoutId = setTimeout(() => {
        callback(evt);
        timeoutId = 0;
      }, interval);
    }
  };
}
