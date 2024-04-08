package main

import (

       "fmt" //this is also important. figure out what most important.
       "log" // we also need to figure out whats in this standard library 
       "os" //Ouuuu she should def memorize what's in this standard library

)

func main() {
//why is there a newline below this... if there's no fucking newline.
    fmt.Println("Ouuu print the filepath mf: ")
//it's weird that print func can initialize w/o being input directily
//into a var
    var filePath string
//var can be defined below print statement. which is weird.
//filepath is defined, and definition has something to do with data type 
    fmt.Scanln(&filePath)
//luckily scan is a standard function in the standard library. yay


    //read the file. the entire file
    content, err := os.ReadFile(filePath)
    if err != nil {
// tf does this error bullshit do
       log.Fatal(err)
      }


      // Print file content to terminal emulator. obvious line
      fmt.Println(string(content))

}