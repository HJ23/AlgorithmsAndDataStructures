package users

type Users interface {
	String() string
	GetPasswordHash() string
	GetRank() int
	IsAdmin() bool
}
