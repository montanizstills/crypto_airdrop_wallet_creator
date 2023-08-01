function printMessage(msg) {
    console.log(msg)
}

function exit(msg){
    throw new Error(msg)
}

module.exports = {
    printMessage: printMessage,
    exit: exit
}
