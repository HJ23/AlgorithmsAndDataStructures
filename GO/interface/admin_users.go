package users

import (
	"fmt"
	"test/utils"
)

type AdminUser struct {
	name         string
	surname      string
	email        string
	passwordHash string
}

func NewAdminUser(name, surname, email, password string) AdminUser {
	passwordHash := utils.MD5(password)
	return AdminUser{name, surname, email, passwordHash}
}

func (u AdminUser) GetName() string {
	return u.name
}

func (u AdminUser) GetSurname() string {
	return u.surname
}

func (u AdminUser) GetEmail() string {
	return u.email
}

func (u AdminUser) GetPasswordHash() string {
	return u.passwordHash
}

func (u AdminUser) GetRank() int {
	return 100
}

func (u AdminUser) IsAdmin() bool {
	return true
}

func (u AdminUser) String() string {
	return fmt.Sprintf("# AdminUser -> {name: %s, surname: %s, email: %s, password_hash: %s}", u.name, u.surname, u.email, u.passwordHash)
}
