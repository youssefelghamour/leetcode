# 2666. Allow One Function Call

Given a function `fn`, return a new function that is identical to the original function except that it ensures `fn` is called **at most once**.

- On the **first call**, it should return the result of `fn`.
- On **subsequent calls**, it should return `undefined`.

## Example 1

- **Input:**  
  `fn = (a, b, c) => a + b + c`  
  `calls = [[1, 2, 3], [2, 3, 6]]`
- **Output:**  
  `[{"calls":1,"value":6}]`
- **Explanation:**
  ```js
  const onceFn = once(fn);
  onceFn(1, 2, 3); // 6
  onceFn(2, 3, 6); // undefined
  ```

## Example 2

- **Input:**  
  `fn = (a, b, c) => a * b * c`  
  `calls = [[5, 7, 4], [2, 3, 6], [4, 6, 8]]`
- **Output:**  
  `[{"calls":1,"value":140}]`
- **Explanation:**
  ```js
  const onceFn = once(fn);
  onceFn(5, 7, 4); // 140
  onceFn(2, 3, 6); // undefined
  onceFn(4, 6, 8); // undefined
  ```

## Constraints

- `calls` is a valid JSON array  
- `1 <= calls.length <= 10`  
- `1 <= calls[i].length <= 100`  
- `2 <= JSON.stringify(calls).length <= 1000`