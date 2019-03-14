import planFlower from '../../code/array/605'

test('planFlower: [0,0,1,0,1], 1', () => {
  expect(planFlower([0, 0, 1, 0, 1], 1)).toBe(true)
})

test('planFlower: [1,0,0,0,1], 1', () => {
  expect(planFlower([0, 0, 1, 0, 1], 1)).toBe(true)
})

test('planFlower: [1,0,0,0,1], 2', () => {
  expect(planFlower([0, 0, 1, 0, 1], 2)).toBe(false)
})