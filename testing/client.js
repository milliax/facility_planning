const zmq = require("zeromq")

async function run() {
  const sock = new zmq.Pull()

  sock.connect("tcp://127.0.0.1:5555")
  console.log("Worker connected to port 5555")

  for await (const [msg] of sock) {
    console.log("work: %s", msg.toString())
  }
}

run()