# 2631. Group By

Enhance all arrays such that you can call the `array.groupBy(fn)` method on any array, returning a grouped version of the array.

A grouped array is an object where each key is the output of `fn(arr[i])` and each value is an array containing all items in the original array which generate that key.

The provided callback `fn` will accept an item in the array and return a string key. The order of each value list should be the order the items appear in the array. Any order of keys is acceptable.

Solve it without lodash's _.groupBy function.

#### Example 1

- **Input:**
  ```javascript
  array = [
    {"id":"1"},
    {"id":"1"},
    {"id":"2"}
  ], 
  fn = function (item) { 
    return item.id; 
  }
  ```

- **Output:**
  ```json
  { 
    "1": [{"id": "1"}, {"id": "1"}],   
    "2": [{"id": "2"}] 
  }
  ```

- **Explanation:**
  Output is from `array.groupBy(fn)`. The selector function gets the "id" out of each item. There are two objects with an "id" of 1, both are grouped together.

#### Example 2

- **Input:**
  ```javascript
  array = [
    [1, 2, 3],
    [1, 3, 5],
    [1, 5, 9]
  ],
  fn = function (list) { 
    return String(list[0]); 
  }
  ```

- **Output:**
  ```json
  { 
    "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]] 
  }
  ```

- **Explanation:**
  The selector function uses the first element as the key. All arrays have 1 as their first element, so they are grouped together.

#### Example 3

- **Input:**
  ```javascript
  array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  fn = function (n) { 
    return String(n > 5);
  }
  ```

- **Output:**
  ```json
  {
    "true": [6, 7, 8, 9, 10],
    "false": [1, 2, 3, 4, 5]
  }
  ```

- **Explanation:**
  The selector function splits the array based on whether each number is greater than 5.

#### Constraints

- `0 <= array.length <= 10^5`
- `fn` returns a string