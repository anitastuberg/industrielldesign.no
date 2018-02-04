// Initiating the canvas
let canvas = document.getElementById('leo-snake')
let ctx = canvas.getContext('2d');

let leoBlue = '#0093bc';
let cellSize = 0;
let cellCount = 50;
let gameStarted = false;
let gameFinished = false;
let logoSize = cellSize * 5;
let speed = 100;
let score = 0;

let validPos = false;

let keyStrokeQueue = [];

let logoTop, logoLeft, heightCenter, widthCenter, windowHeight, windowWidth, direction;
let requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;

let backgroundSize = 0;


function drawSquare(x, y, colour) {
    ctx.fillStyle = colour;
    ctx.fillRect(x, y, cellSize, cellSize);
}

$(document).keyup(function (e) {
    let key = e.which;
    if ((key === 37 || key === 38 || key === 39 || key === 40)) {
        if (!gameStarted) {
            gameStarted = true;
            game();
        } else {
            keyStrokeQueue.push(key);
        }

    }
});

function drawBackground() {
    ctx.fillStyle = leoBlue;
    ctx.fillRect(0, 0, windowWidth, windowHeight);
}

function drawLogoBackground(x, y, size) {
    // Large rect
    ctx.fillStyle = leoBlue;
    ctx.fillRect(x, y, size, size);
}

function changeSize() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    canvas.setAttribute('width', windowWidth);
    canvas.setAttribute('height', windowHeight);
    calculateCellSize(windowWidth);
    widthCenter = windowWidth / 2;
    heightCenter = windowHeight / 2;
    logoLeft = widthCenter - logoSize / 2; // Leftmost side of logo
    logoTop = heightCenter - logoSize / 2; // Top of logo
    drawLogoBackground(logoLeft, logoTop, logoSize, logoSize);
    if (windowHeight < windowWidth) {
        backgroundSize = windowWidth;
    } else {
        backgroundSize = windowHeight;
    }
}

function updateSnakeApple() {
    snake.draw();
    apple.draw();
}

function calculateCellSize(windowWidth) {
    cellSize = Math.floor(windowWidth / cellCount);
    logoSize = cellSize * 5;
}

function clearScreen() {
    ctx.clearRect(0, 0, windowWidth, windowHeight);
}

function backgroundAnimation() {
    clearScreen();
    drawLogoBackground(fillX, fillY, fillSize);
    apple.draw();
    snake.draw();

    fillSize += 50;
    fillX -= 25;
    fillY -= 25;

    if (fillSize < backgroundSize + 100) {
        requestAnimationFrame(backgroundAnimation);
    }
}

function backgroundAnimationReset() {
    if (fillSize > logoSize) {
        requestAnimationFrame(backgroundAnimationReset);
    } else {
        location.reload();
    }
    clearScreen();
    drawLogoBackground(fillX, fillY, fillSize);
    apple.draw();
    snake.draw();
    fillSize -= 50;
    fillX += 25;
    fillY += 25;

}

class Snake {
    constructor() {
        this.direction = 'up';
        this.prevDirection = 'up';
        this.snakeStart = [{
                x: logoLeft + cellSize,
                y: logoTop + cellSize
            },
            {
                x: logoLeft + cellSize,
                y: logoTop + cellSize * 2
            },
            {
                x: logoLeft + cellSize,
                y: logoTop + cellSize * 3
            },
            {
                x: logoLeft + cellSize * 2,
                y: logoTop + cellSize * 3
            },
            {
                x: logoLeft + cellSize * 3,
                y: logoTop + cellSize * 3
            }
        ]
        this.snake = this.snakeStart;
    }

    draw() {
        // L
        if (!gameStarted) {
            ctx.fillStyle = 'white';
            ctx.fillRect(logoLeft + cellSize, logoTop + cellSize, cellSize, cellSize * 3);
            ctx.fillStyle = 'white';
            ctx.fillRect(logoLeft + cellSize, logoTop + cellSize * 3, cellSize * 3, cellSize);
        } else {

            for (let i = 0; i < this.snake.length - 1; i++) {
                ctx.fillStyle = 'white';
                ctx.fillRect(this.snake[i].x, this.snake[i].y, cellSize -2, cellSize -2);
            }
        }
    }

    move() {
        if (this.direction === 'up' ) {
            this.snake.unshift({
                x: this.snake[0].x,
                y: this.snake[0].y - cellSize
            });
        }
        else if (this.direction === 'right' ) {
            this.snake.unshift({
                x: this.snake[0].x + cellSize,
                y: this.snake[0].y
            });
        }
        else if (this.direction === 'down' ) {
            this.snake.unshift({
                x: this.snake[0].x,
                y: this.snake[0].y + cellSize
            });
        }
        else if (this.direction === 'left' ) {
            this.snake.unshift({
                x: this.snake[0].x - cellSize,
                y: this.snake[0].y
            });
        }
        ctx.fillStyle = leoBlue;
        ctx.fillRect(this.snake[this.snake.length - 1].x - 1, this.snake[this.snake.length - 1].y - 1, cellSize + 2, cellSize + 2);
        this.draw();
    }

    changeDirection() {
        if (keyStrokeQueue.length > 0) {
            let key = keyStrokeQueue.shift();
            if (key === 38 && this.direction !== 'down') {
                this.direction = 'up';
            } else if (key === 39 && this.direction !== 'left') {
                this.direction = 'right';
            } else if (key === 40 && this.direction !== 'up') {
                this.direction = 'down';
            } else if (key === 37 && this.direction !== 'right') {
                this.direction = 'left';
            }
        }
    }

    isDead() {
        if (this.snake[0].x < 0 ||
            this.snake[0].x > windowWidth - cellSize ||
            this.snake[0].y < 0 ||
            this.snake[0].y > windowHeight - cellSize
        ) {
            gameFinished = true;
        }
        for (let i = 1; i < this.snake.length; i++) {
            if (this.snake[0].x === this.snake[i].x && this.snake[0].y === this.snake[i].y) {
                gameFinished = true;
                break;
            }
        }
    }
}

class Apple {
    constructor() {
        this.startPos = {
            x: logoLeft + cellSize * 3,
            y: logoTop + cellSize
        }
        this.applePos = {
            x: this.startPos.x,
            y: this.startPos.y
        };
    }

    draw() {
        ctx.fillStyle = 'white';
        ctx.fillRect(this.applePos.x, this.applePos.y, cellSize - 2, cellSize - 2);
    }

    updatePos() {
        while (!validPos) {
            this.applePos.x = this.startPos.x + Math.floor(Math.random() * windowWidth / cellSize / 2) * cellSize;
            this.applePos.y = this.startPos.y + Math.floor(Math.random() * windowHeight / cellSize / 2) * cellSize;
            for (let i = 0; i < snake.snake.length; i++) {
                if (this.applePos.x === snake.snake[i].x && this.applePos.x === snake.snake[i].y) {
                    validPos = false;
                    break;
                }
                validPos = true;
            }
            if (this.applePos.x > windowWidth - cellSize || this.applePos.x < 0 || this.applePos.y < 0 || this.applePos.y > windowHeight - cellSize) {
                validPos = false;
            }
        }
        validPos = false;
        this.draw();
    }

    isEaten() {
        let appleEaten = false;
        for (let i = 0; i < snake.snake.length; i++) {
            if (snake.snake[i].x == this.applePos.x && snake.snake[i].y == this.applePos.y) {
                if (i > 0) {
                    console.log('Bug fix working');
                }
                appleEaten = true;
                break;
            } 
        }
        if (appleEaten) {
            score++;
            speed *= 2;
            this.updatePos();
        } else {
            snake.snake.pop();
        }
    }
}

changeSize();
let snake = new Snake();
let apple = new Apple();

let fillX, fillY, fillSize;

function setup() {

    changeSize();
    drawLogoBackground(logoLeft, logoTop, logoSize);
    updateSnakeApple();
    $(window).resize(() => {
        changeSize()
        updateSnakeApple();
    });
}

function game() {

    fillX = logoLeft;
    fillY = logoTop;
    fillSize = logoSize;

    backgroundAnimation();

    let gameLoopInterval = setInterval(gameLoop, speed);

    function gameLoop() {
        snake.changeDirection();
        snake.move();
        snake.isDead();
        apple.isEaten();
        if (gameFinished) {
            clearInterval(gameLoopInterval);
            backgroundAnimationReset();
        }
    }
}




setup();