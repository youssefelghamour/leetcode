# 2722. Join Two Arrays by ID

Given two arrays `arr1` and `arr2`, return a new array `joinedArray` formed by merging `arr1` and `arr2` based on their `id` key. 

- The length of `joinedArray` should be the length of unique values of `id`.
- The returned array should be sorted in ascending order based on the `id` key.


If a given `id` exists in one array but not the other, include the single object with that `id` without modification.
If two objects share an `id`, merge their properties:

- If a key exists in only one object, include that key-value pair.
- If a key exists in both objects, the value from `arr2` overrides the value from `arr1`.

#### Example 1

- **Input:**
  ```javascript
  arr1 = [
      {"id": 1, "x": 1},
      {"id": 2, "x": 9}
  ], 
  arr2 = [
      {"id": 3, "x": 5}
  ]
  ```

- **Output:**
  ```json
  [
      {"id": 1, "x": 1},
      {"id": 2, "x": 9},
      {"id": 3, "x": 5}
  ]
  ```

- **Explanation:** No duplicate `id`s; `arr1` is concatenated with `arr2`.

#### Example 2

- **Input:**
  ```javascript
  arr1 = [
      {"id": 1, "x": 2, "y": 3},
      {"id": 2, "x": 3, "y": 6}
  ], 
  arr2 = [
      {"id": 2, "x": 10, "y": 20},
      {"id": 3, "x": 0, "y": 0}
  ]
  ```

- **Output:**
  ```json
  [
      {"id": 1, "x": 2, "y": 3},
      {"id": 2, "x": 10, "y": 20},
      {"id": 3, "x": 0, "y": 0}
  ]
  ```

- **Explanation:** Objects with `id=2` are merged; keys from `arr2` override those in `arr1`.

#### Example 3

- **Input:**
  ```javascript
  arr1 = [
      {"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}
  ]
  arr2 = [
      {"id": 1, "b": {"c": 84}, "v": [1, 3]}
  ]
  ```

- **Output:**
  ```json
  [
      {"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}
  ]
  ```

- **Explanation:** Objects with `id=1` are merged. The values from `arr2` are used for keys "b" and "v". Key "y" is only in `arr1`.

#### Constraints

- `arr1` and `arr2` are valid JSON arrays
- Each object in `arr1` and `arr2` has a unique integer `id` key
- `2 <= JSON.stringify(arr1).length <= 10^6`
- `2 <= JSON.stringify(arr2).length <= 10^6`