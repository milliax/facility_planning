const zmq = require("zeromq")

async function run() {
    const sock = new zmq.Subscriber()

    sock.connect("tcp://127.0.0.1:5555")
    sock.subscribe("")
    console.log("Subscriber connected to port 5555")

    for await (const [msg] of sock) {
        console.log(
            "received a message related to:",
        )
        console.log(msg.toString())
    }
}

run()
