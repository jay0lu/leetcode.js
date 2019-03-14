export default (flowerbed, n) => {
  let max = 0
  flowerbed.push(0)
  flowerbed.unshift(0)
  for (let i = 1; i < flowerbed.length - 1; i++) {
    if (flowerbed[i] === 0 && flowerbed[i - 1] === 0 && flowerbed[i + 1] === 0) {
      max += 1
      i += 1
    }
  }
  return max >= n
}