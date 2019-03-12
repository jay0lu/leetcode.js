// export default (deck) => {
//   let sortedDeck = deck.sort((a, b) => a - b)
//   let minLen = Number.MAX_SAFE_INTEGER
//   let dst = []
//   let result = true

//   if (deck.length === 1) return false

//   for (let i = 0, len = sortedDeck.length, tmp = []; i < len; i++) {
//     tmp.push(sortedDeck[i])
//     for (let j = i + 1; j < len - 1; j++) {
//       if (sortedDeck[i] === sortedDeck[j]) {
//         tmp.push(sortedDeck[j])
//       } else {
//         if (minLen > tmp.length) {
//           minLen = tmp.length
//         }
//         dst.push([].concat(tmp))
//         tmp.length = 0
//         i = j
//       }
//     }
//   }

//   dst.every(item => {
//     if (item.length % minLen !== 0) {
//       result = false
//       return false
//     }
//   })

//   return result
// }

// 获得两个数的最大公约数
function getBigFactor (a, b) {
  return b === 0 ? a : getBigFactor(b, a % b)
}
export default (arr) => {
  arr.sort((a, b) => a - b)
  let dst = []
  let result = true
  let radix = Number.MAX_SAFE_INTEGER
  for (let i = 0, len = arr.length, tmp = []; i < len; i++) {
    tmp.push(arr[i])
    for (let j = i + 1; j <= len; j++) {
      if (arr[i] === arr[j]) {
        tmp.push(arr[j])
      } else {
        if (i === 0) {
          // 第一次循环, 基数为该数字分组的长度
          radix = tmp.length
        } else {
          // 获取所有分组长度的最大公约数
          let temp = getBigFactor(radix, tmp.length)
          radix = temp < radix ? temp : radix
        }
        dst.push([].concat(tmp))
        tmp.length = 0
        i = j - 1
        break
      }
    }
  }
  console.log(dst)
  console.log(radix)
  dst.every(item => {
    if (item.length % radix !== 0) {
      result = false
      return false
    } else {
      return true
    }
  })
  return radix > 1 && result
}