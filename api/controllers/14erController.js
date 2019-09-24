
var dbconfig = {
        server: '',
        user: 'SA',
        password: '',
        database: 'mountains',
        port: 1433,
        options: {
            encrypt: false
        }
    };
var sql = require('mssql')


exports.list_all_14ers = function(req, res) {
    const conn = new sql.ConnectionPool(dbconfig);
    conn.connect(err => {
        if (err) throw err;
            req = new sql.Request(conn);
            // INSERT INTO mountains.dbo.thirteeners (name) VALUES ('${name})'
            req.query(`SELECT * FROM mountains.dbo.thirteeners `, (err, recordset) => {
                if(err) throw err;
            conn.close();
            const data = recordset.recordset;
            res.json(data)
            })
    })
}

exports.get_mountain = function(req, res){
    var data;
    var name = req.params.mountain;
    var conn = new sql.ConnectionPool(dbconfig);
    conn.connect(err => {
        
        if (err) throw err;
        var req = new sql.Request(conn);
        
            // INSERT INTO mountains.dbo.thirteeners (name) VALUES ('${name})'
            
            req.query(`SELECT peak, elevation, ranges FROM mountains.dbo.thirteeners WHERE ranges = '${name}' `, (err, recordset) => {
                if(err) throw err;
                
                   // console.log(JSON.stringify(reco   rdset.recordset));
                    conn.close();
                  //  console.log(conn)
                data = recordset.recordset;
            
               
               res.json(data)
                
            })
            
    })
}

