// export default (digits) => {
//   const obj = {
//     2: "abc",
//     3: "def",
//     4: "ghi",
//     5: "jkl",
//     6: "mno",
//     7: "pqrs",
//     8: "tuv",
//     9: "wxyz"
//   };
//   let num = digits.split('');
//   let code = [];

//   if (num.length < 1) return [];

//   num.forEach(n => {
//     code.push(obj[n]);
//   });

//   if (num.length <= 1) return code[0].split('');

//   let comb = (arr) => {
//     let tmp = [];
//     for (let i = 0, iLen = arr[0].length; i < iLen; i++) {
//       for (let j = 0, jLen = arr[1].length; j < jLen; j++) {
//         tmp.push(`${arr[0][i]}${arr[1][j]}`);
//       }
//     }
//     arr.splice(0, 2, tmp);

//     if (arr.length > 1) {
//       comb(arr);
//     } else {
//       return tmp;
//     }

//     return arr[0];
//   };

//   return comb(code);
// };

export default (digits) => {
  if (!digits.length) return []
  let arr = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

  let multiply = (arr1, arr2) => {
    let innerRes = []
    for (let i = 0, len1 = arr1.length; i < len1; ++i) {
      for (let j = 0, len2 = arr2.length; j < len2; ++j) {
        innerRes.push(arr1[i] + arr2[j])
      }
    }
    return innerRes
  }

  return digits.split('').reduce((prev, cur) => {
    return multiply(prev, arr[Number(cur)])
  }, [''])
}