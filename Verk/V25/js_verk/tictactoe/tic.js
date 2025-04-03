let player = "X";

function playerMove(event) {
    let section = event.target;
    section.innerHTML = player;

    //checks if legal
    if (legalMoves(section)) {
        section.innerHTML = player;

        if (checkWin)
            player = "O";
        setTimeout(computerMove(), 1000);
    } else {
        alert("Illegal move, choose another box");
    }
}

function computerMove() {
    let legalGames = [];
    for (let i = 1; i < 10; i++) {
        let section = document.getElementById(i);
        if (legalMoves(section)) {
            legalGames.push(section);
        }
    }

    let chosenNumber = Math.floor(Math.random() * legalGames.length);
    let chosenSection = legalGames[chosenNumber];
    chosenSection.innerHTML = player;

    player = "X";
}

// checks if move is legal
function legalMoves(square) {
    if (square.innerHTML === "") {
        return true;
    } else {
        return false;
    }
}

//function that check if someone has won the game
function checkWin() {
    let winCondition = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ];
    let counter = 0;
    for (let i = 0; i < winCondition.length; i++) {
        for (let j = 0; j < 3; j++) {
            let section = document.getElementById(winCondition[i][j])
            if (section.innerHTML === player) {
                counter++;
            }
        }
        if (counter === 3) {
            return true;
        }
    }
    return false;
}

document.getElementById('gameBoard').addEventListener('click', playerMove);