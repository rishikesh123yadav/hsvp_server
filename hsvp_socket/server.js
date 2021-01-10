var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);
var mysql = require('mysql');
//var sqlite3 = require('sqlite3').verbose();

// open the database

/*let db = new sqlite3.Database('/home/rishikesh/cmm/projects/hsvp_server/hsvp_server/db.sqlite3',sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the hsvp_server database.');
});
*/

/* Creating POOL MySQL connection.*/

var pool=mysql.createPool({
      connectionLimit   :   100,
      host              :   'localhost',
      user              :   'root',
      password          :   '123456',
      database          :   'Test',
      debug             :   false
});

app.get("/",function(req,res){
    res.sendFile(__dirname + '/index.html');
});

var clients = 0;
io.on('connection',function(socket){  
    clients++;
    //io.sockets.emit('broadcast',{ description: clients + ' clients connected!'});
    console.log(clients + '  clients connected !!');
    pool.query('SELECT * FROM student', function(err,rows){
    if(err)throw err;
    //console.log(rows);
    io.sockets.emit('showrows',rows);
});

    socket.on('status added',function(status){
      add_status(status,function(res){
        if(res){
            io.emit('refresh feed',status);
        } else {
            io.emit('error');
        }
      });
    });
    socket.on('disconnect', function () {
    clients--;
    console.log( clients + '  clients connected !!');
   });
});


var add_status = function (status,callback) {
    pool.getConnection(function(err,connection){
        if (err) {
          callback(false);
          return;
        }
    connection.query("INSERT INTO `fbstatus` (`s_text`) VALUES ('"+status+"')",function(err,rows){
            connection.release();
            if(!err) {
              callback(true);
            }
        });
    connection.on('error', function(err) {
              callback(false);
              return;
        });
    });
}

http.listen(3000, () => {
  console.log('Server is up and running on port: 3000.....');
});