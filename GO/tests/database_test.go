package tests

import (
	"fmt"
	database "test/generics"
	users "test/interface"
	"testing"
)

var databaseObj database.Database[users.Users]

func init() {
	obj1 := users.NewRegularUser("John", "Connor", "abc@mail.com", "Password123")
	obj2 := users.NewAdminUser("John", "Connor", "abc@mail.com", "Password123")

	databaseObj = database.Database[users.Users]{}
	databaseObj.Add(obj1)
	databaseObj.Add(obj2)
	fmt.Println(databaseObj)

}

func TestDatabaseAddingFunctionality(t *testing.T) {
	var want int64 = 2
	have := databaseObj.GetSize()

	if want != have {
		t.Fatalf("# Error in database adding functionality sizes don't match")
	}

}
