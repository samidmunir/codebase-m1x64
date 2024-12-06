/*
    variables program
    - main.rs
*/

fn main() {
    println!("Variables in Rust!");

    /*
        Variables
        - Assigned using the "let" keyword.
        - Print to standard output by print!() or println!().
        - Scope of a variable is defined by the block of code in which it is declared.
        - Function is a named block of code that is reusable.
        - Shadowing allows a variable to be re-declared in the same scope with the same name.
    */

    /*
        Binding & Mutability
        - a variable can be used only if it has been initialized.
        - by default, all variables in its nature are immutable.
            > use the mut keyword to make a variable mutable.
    */
    // let x: i32; // uninitialized but used, ERROR!
    let x: i32 = 7; // uninitialized but also unused, only a WARNING!
    // println!("x: {}", x);
    println!("\n(1) x: {}", x); 

    let mut x: i8 = 77;
    println!("\n(2) x (before): {}", x);
    x = x + 12;
    println!("(2) x (after): {}", x);

    /*
        Scope
        - a scope is the range within the program for which the item is valid.
    */
    let x: i8 = 10;
    let y: i8 = 123;
    {
        let y: i8 = 5;
        println!("\n(inner) x is {} | y is {}", x, y);
    }
    println!("(outer) x is {} | y is {}", x, y);

    define_x();

    /*
        Shadowing
        - declaring a new variable with the same name as a previous variable (the first one is shadowed by the second one).
    */
    let x: u8 = 5;
    println!("\n(1) (outer) x: {}", x);
    {
        let x: u8 = 12;
        println!("(inner) x: {}", x);
    }
    let x: u8 = 42;
    println!("(2) (outer) x: {}", x);

    /*
        Shadowing & rebinding
    */
    let mut x: u8 = 1;
    x = 7;
    let x = x;
    // x = x + 3; // cannot do this because by default x is immutable.

    let y: u8 = 7;
    let y: &str = "Hello world!";

    /*
        Prepend variable name with _ to remove warnings for unused variables.

        Also possible to use:
            #[allow(unused_variables)]
    */
}

fn define_x() {
    let x: &str = "hello";
    println!("\ndefine_x() called...");
    println!("\tx: {}", x);
}