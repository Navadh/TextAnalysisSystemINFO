function editConfirm() {
            var con=confirm("Are you sure to you want to edit the user?");
                if (con==true)
                    {
                    window.open("EditUser.html", "main");
                    }
                else
                    alert('No!');

            }

function addConfirm() {
            var con=confirm("Are you sure to you want to add new user?");
                if (con==true)
                    {
                    window.open("AddUser.html", "main");
                    }
                else
                    alert('No!');

            }

function delConfirm() {
            var con=confirm("This action cannot be reversed, are you sure to delete it?");
                if (con==true)
                    {
                    alert('Done!');
                    }
                else
                    alert('No!');

            }

