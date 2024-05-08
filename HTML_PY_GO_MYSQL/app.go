package main

import (
	"database/sql"
	"net/http"

	// https://pkg.go.dev/github.com/gin-gonic/gin
	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
)

var db *sql.DB

func main() {
	// Initialize the MySQL database connection
	var err error
	db, err = sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/kvsp_paul")
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	// Initialize the Gin router
	router := gin.Default()

	// Define the route handlers
	router.LoadHTMLGlob("templates/*")
	router.GET("/", showForm)
	router.POST("/", submitForm)

	// Start the server
	router.Run(":8081")
}

func showForm(c *gin.Context) {
	c.HTML(http.StatusOK, "Form.html", nil)
}

func submitForm(c *gin.Context) {
	// Retrieve form data
	username := c.PostForm("name")
	email := c.PostForm("email")

	// Insert data into the database
	_, err := db.Exec("INSERT INTO pygo (name, email) VALUES (?, ?)", username, email)
	if err != nil {
		c.String(http.StatusInternalServerError, "Error inserting data into the database")
		return
	}

	c.String(http.StatusOK, "Success_go")
}
