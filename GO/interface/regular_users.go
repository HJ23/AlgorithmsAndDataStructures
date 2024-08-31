package users

import (
	"fmt"
	"test/utils"
)

type RegularUser struct {
	name         string
	surname      string
	email        string
	passwordHash string
}

func NewRegularUser(name, surname, email, password string) RegularUser {
	passwordHash := utils.MD5(password)
	return RegularUser{name, surname, email, passwordHash}
}

func (u RegularUser) GetName() string {
	return u.name
}

func (u RegularUser) GetSurname() string {
	return u.surname
}

func (u RegularUser) GetEmail() string {
	return u.email
}

func (u RegularUser) GetPasswordHash() string {
	return u.passwordHash
}

func (u RegularUser) GetRank() int {
	return 0
}

func (u RegularUser) IsAdmin() bool {
	return false
}

func (u RegularUser) String() string {
	return fmt.Sprintf("# RegularUser -> {name: %s, surname: %s, email: %s, password_hash: %s}", u.name, u.surname, u.email, u.passwordHash)
}
