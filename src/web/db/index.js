const {
  Pool
} = require('pg')

// TODO: update this to point to our test server with correct credentials
const pool = new Pool({
  user: 'nodejs',
  host: '127.0.0.1',
  database: 'books',
  password: '',
  port: 5432,
})

module.exports = {
  query: (text, params) => {
    return pool.query(text, params)
  },
  pool: pool
}