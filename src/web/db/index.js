const {
  Pool
} = require('pg')

// TODO: update this to point to our test server with correct credentials
const pool = new Pool({
  user: 'ece651_web',
  host: '127.0.0.1',
  database: 'ece651',
  password: 'dm2fBdodbrHPtJVvlSKF',
  port: 5432,
})

module.exports = {
  query: (text, params) => {
    return pool.query(text, params)
  },
  pool: pool
}