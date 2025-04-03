// Fundamentals
let box = 32; // size of boxes
let gameSpeed = 125; // speed of game
let direction; //direction of snake
let score = 0; // scored points

const c = document.getElementById('gameBoard');
const ctx = c.getContext('2d');
// snake
let snake = [];
snake[0] = {
    x: 9 * box,
    y: 10 * box
}

let apple = {
    x: Math.floor(Math.random() * 17 + 1) * box,
    y: Math.floor(Math.random() * 15 + 3) * box
}

// Fetch images
let ground = new Image();
ground.src = 'images/ground.png'
let food = new Image();
food.src = 'images/food.png'

// Drawing function
function draw() {

}

// change direction
function directionSnake(event) {
    if (event.key === "ArrowUp" && direction != "down") {
        direction = "up"
    }
    else if (event.key === "ArrowDown" && direction != "up") {
        direction = "down"
    }
    else if (event.key === "ArrowRight" && direction != "left") {
        direction = "left"
    }
    else if (event.key === "ArrowLeft" && direction != "right") {
        direction = "right"
    }
}
let newHead = {
    x: snake[0].x,
    y: snake[0].y
}

if (direction === "left") newHead.x -= box;
if (direction === "right") newHead.x += box;
if (direction === "up") newHead.x -= box;
if (direction === "down") newHead.x += box;

snake.upshift(newHead);
snake.pop();

document.addEventListener('keydown', directionSnake);

//function that draws everything
function draw() {
    ctx.drawImage(ground, 0, 0);
    ctx.drawImage(food, apple.x, apple.y);
    ctx.font = "42px Arial";
    ctx.fillStyle = "white";
    ctx.fillText(score, 2.2 * box, 1.6 * box);

    for (let i = 0; i < snake.length; i++) {
        if (i === 0) {
            ctx.fillStyle = "green";
        }
        else {
            ctx.fillStyle = "white";
        }
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
    }
}