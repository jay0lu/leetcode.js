import deckGroup from '../../code/array/914'

test('deckGroup: [1,2,3,4,4,3,2,1]', () => {
  expect(deckGroup([1, 2, 3, 4, 4, 3, 2, 1])).toBe(true)
})

test('deckGroup: [0,0,0,1,1,1,2,2,2]', () => {
  expect(deckGroup([0, 0, 0, 1, 1, 1, 2, 2, 2])).toBe(true)
})

test('deckGroup: [1]', () => {
  expect(deckGroup([1])).toBe(false)
})

test('deckGroup: [1,1]', () => {
  expect(deckGroup([1, 1])).toBe(true)
})

test('deckGroup: [1,1,2,2,2,2]', () => {
  expect(deckGroup([1, 1, 2, 2, 2, 2])).toBe(true)
})