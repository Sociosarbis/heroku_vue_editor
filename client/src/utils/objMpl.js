export function mergeLeft(left, right) {
  const newObj = { ...left };
  Object.keys(right).forEach((key) => {
    if (newObj[key] !== undefined) {
      newObj[key] = right[key];
    }
  });
  return newObj;
}

export default {
  mergeLeft,
};
