/*
PROBLEM DESCRIPTION:
Write a function expect that helps developers test their code. It should
take in any value val and return an object with the following two functions.
toBe(val) accepts another value and returns true if the two values === each other.
If they are not equal, it should throw an error "Not Equal".
notToBe(val) accepts another value and returns true if the two values
!== each other. If they are equal, it should throw an error "Equal".
EXAMPLE:
Input: func = () => expect(5).toBe(5)
Output: {"value": true}
Explanation: 5 === 5 so this expression returns true.
*/

let expect = (val) => {
  return {
    toBe: (value) => {
      if (val !== value) throw new Error("Not Equal")
      else return true;
    },
    notToBe: (value) => {
      if (val === value) throw new Error("Equal")
      else return true
    }
  }
}

console.log(expect(5).notToBe(null))