console.log("hello");

const alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

let count=0


for (let l=1;l<6;l++){

    
}


const strings = alphabet.forEach((letter1)=>{
    alphabet.forEach((letter2)=>{
        alphabet.forEach((letter3)=>{


            let word =  letter1+letter2+letter3
            if (((letter1>=letter2 && letter2>= letter3))){

                console.log(word);
            }
            else if (((letter1<=letter2 && letter2<= letter3))){

                console.log(word);
            }
            else{
                count+=1
                console.log(word);
                console.log(count);

            }
            
    
        })
    })
})

console.log(count);