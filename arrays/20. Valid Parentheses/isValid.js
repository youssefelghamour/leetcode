/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const matchingBrackets = {
          ')': '(',
          '}': '{',
          ']': '['
      };
  
      const stack = [];
  
      for (let c of s) {
          if (Object.values(matchingBrackets).includes(c)) {  // Opening brackets
              stack.push(c);
          } else if (c in matchingBrackets) {  // Closing brackets
              if (stack.length === 0 || stack.pop() !== matchingBrackets[c]) {
                  return false;
              }
          }
      }
  
      return stack.length === 0;  
  };