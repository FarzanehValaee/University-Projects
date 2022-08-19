import java.io.*;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws IOException {


        File newFile = new File("C:/Users/Saleh/Downloads/Compressed/Compiler/input.txt");

//Create  A ArrayList For Storing Characters
        ArrayList arrayList = new ArrayList();


//Read A File Char by Char
        FileReader fr = new FileReader(newFile);
        BufferedReader br = new BufferedReader(fr);
        int c = 0;


//Storing Characters in ArrayList
        while ((c = br.read()) != -1) {
            char character = (char) c;
            arrayList.add(character);
        }


//Searching the Array For Lexemes
        int counter = 0;
        int lineNumber = 1;
        char otherInput = ' ';
        String state = "start";

        while (counter < arrayList.size()) {


            if (state.equals("start")) {
                if (arrayList.get(counter).equals('w')) {
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    otherInput =(Character) arrayList.get(counter);
                    state = "otherop";
                }

            }

            else if (state.equals("w")) {
                if (arrayList.get(counter).equals('h')) {
                    state = "wh";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("wh")) {
                if (arrayList.get(counter).equals('i')) {
                    state = "whi";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("whi")) {
                if (arrayList.get(counter).equals('l')) {
                    state = "whil";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("whil")) {
                if (arrayList.get(counter).equals('e')) {
                    state = "while";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("while")) {
                if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< KEYWORD , WHILE >");
                    System.out.println("< NEW LINE , /n >");
                    state = "key:while";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< KEYWORD , WHILE >");
                    state = "key:while";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< KEYWORD , WHILE >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< KEYWORD , WHILE >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< KEYWORD , WHILE >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< KEYWORD , WHILE >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< KEYWORD , WHILE >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("key:while")) {
                if (arrayList.get(counter).equals('w')) {
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("f")) {
                if (arrayList.get(counter).equals('o')) {
                    state = "fo";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("fo")) {
                if (arrayList.get(counter).equals('r')) {
                    state = "for";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput =(Character)  arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("for")) {
                if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< KEYWORD , FOR >");
                    System.out.println("< NEW LINE , /n >");
                    state = "key:for";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< KEYWORD , FOR >");
                    state = "key:for";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< KEYWORD , FOR >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< KEYWORD , FOR >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< KEYWORD , FOR >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< KEYWORD , FOR >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< KEYWORD , FOR >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("key:for")) {
                if (arrayList.get(counter).equals('w')) {
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("i")) {
                if (arrayList.get(counter).equals('f')) {
                    state = "if";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< IDENTIFIER , "+state+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("if")) {
                if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< KEYWORD , IF >");
                    System.out.println("< NEW LINE , /n >");
                    state = "key:if";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< KEYWORD , IF >");
                    state = "key:if";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< KEYWORD , IF >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< KEYWORD , IF >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< KEYWORD , IF >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< KEYWORD , IF >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< KEYWORD , IF >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("key:if")) {
                if (arrayList.get(counter).equals('w')) {
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("identifier")) {
                if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "identifier";
                }

                else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "identifier";
                }

                else if (arrayList.get(counter).equals('_')) {
                    state = "identifier";
                }

                else if (arrayList.get(counter).equals('\n')) {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                }

                else if (arrayList.get(counter).equals(' ')) {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "start";
                }

                else if (arrayList.get(counter).equals('(')) {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "(";
                }

                else if (arrayList.get(counter).equals(')')) {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = ")";
                }

                else if (arrayList.get(counter).equals('+')) {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "+";
                }

                else if (arrayList.get(counter).equals('=')) {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "=";
                }

                else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.print("< IDENTIFIER , ");

                    int temp = counter;
                    temp--;
                    while ((arrayList.get(temp).equals('_') || Character.isLetter((Character) arrayList.get(temp)) || Character.isDigit((Character) arrayList.get(temp))))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("integer")) {
                if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "error";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                }
                else if (arrayList.get(counter).equals(' ')) {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "start";
                }
                else if (arrayList.get(counter).equals('(')) {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "(";
                }
                else if (arrayList.get(counter).equals(')')) {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = ")";
                }
                else if (arrayList.get(counter).equals('+')) {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "+";
                }
                else if (arrayList.get(counter).equals('=')) {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();


                    state = "=";
                }
                else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                }

                else if ((arrayList.get(counter).equals('-') || arrayList.get(counter).equals('/') || arrayList.get(counter).equals('%') || arrayList.get(counter).equals('*') || arrayList.get(counter).equals('!') || arrayList.get(counter).equals(';') || arrayList.get(counter).equals('<') || arrayList.get(counter).equals('>'))){
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();
                    state = "start";
                }

                else {
                    System.out.print("< INTEGER , ");

                    int temp = counter;
                    temp--;
                    while (Character.isDigit((Character) arrayList.get(temp)))
                        temp--;
                    temp++;
                    while (temp<counter){
                        System.out.print(arrayList.get(temp));
                        temp++;
                    }

                    System.out.print(" >");

                    System.out.println();
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("error")) {
                if (Character.isLetter((Character) arrayList.get(counter))) {
                    state = "error";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    state = "error";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("Invalid input in Line: " + lineNumber);
                    otherInput = (Character) arrayList.get(counter);
                    state = "error";
                }
            }

            else if (state.equals("+")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , + >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , + >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , + >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , + >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , + >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< OPERATOR , + >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , + >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , + >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , + >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    state = "++";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< OPERATOR , + >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , + >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("(")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , ( >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , ( >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< OPERATOR , ( >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , ( >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< OPERATOR , ( >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , ( >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals(")")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , ) >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , ) >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< OPERATOR , ) >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , ) >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< OPERATOR , ) >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , ) >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("=")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , = >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , = >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , = >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , = >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , = >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< OPERATOR , = >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , = >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , = >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , = >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< OPERATOR , = >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    state = "==";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , = >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("++")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< OPERATOR , ++ >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< OPERATOR , ++ >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , ++ >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("==")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , == >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , == >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , == >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , == >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , == >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< OPERATOR , == >");
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , == >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , == >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , == >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< OPERATOR , == >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< OPERATOR , == >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , == >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }

            else if (state.equals("otherop")){
                if (arrayList.get(counter).equals('w')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "w";
                } else if (arrayList.get(counter).equals('f')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "f";
                } else if (arrayList.get(counter).equals('i')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "i";
                } else if (Character.isLetter((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "identifier";
                } else if (Character.isDigit((Character) arrayList.get(counter))) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "integer";
                } else if (arrayList.get(counter).equals('\n')) {
                    System.out.println("< NEW LINE , /n >");
                    state = "start";
                    lineNumber++;
                } else if (arrayList.get(counter).equals(' ')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "start";
                } else if (arrayList.get(counter).equals('(')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "(";
                } else if (arrayList.get(counter).equals(')')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = ")";
                } else if (arrayList.get(counter).equals('+')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "+";
                } else if (arrayList.get(counter).equals('=')) {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    state = "=";
                } else if (arrayList.get(counter).equals('@')) {
                    System.out.println("Invalid character in Line: " + lineNumber);
                    state = "error";
                } else {
                    System.out.println("< OPERATOR , "+otherInput+" >");
                    otherInput = (Character) arrayList.get(counter);
                    state = "otherop";
                }
            }



            counter++;
        }
    }
}