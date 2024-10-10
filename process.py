package main
import (
"bufio"
"fmt"
"os"
)
func main() {
r := bufio.NewReader(os.Stdin)
fmt.Print("Enter a string: ")
s, _ := r.ReadString('\n')
var f [256]int
for i := 0; i < len(s); i++ {
ch := s[i]
f[ch]++
}
var res byte
for i := 0; i < len(s); i++ {
if f[s[i]] == 1 {
res = s[i]
break
}
}
if res != 13 {
fmt.Printf("first non repeating character:%c", res)
} else {
fmt.Printf("not found")
}
}
