function editConfirm() {
            var con=confirm("Are you sure to you want to edit the user?");
                if (con==true)
                    {
                    window.open(url="/usermanage/edituser", "main");
                    }
                else
                    alert('No!');

            }

function addConfirm() {
            var con=confirm("Are you sure to you want to add new user?");
                if (con==true)
                    {
                    window.open(url="/usermanage/useradd", "main");
                    }
                else
                    alert('No!');

            }

function delConfirm() {
            var con=confirm("This action cannot be reversed, are you sure to delete it?");
                if (con==true)
                    {
                    window.open(url="/usermanage/userdelete", "main");
                    }
                else
                    alert('No!');

            }