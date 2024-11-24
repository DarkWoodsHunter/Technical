export default function MainLoging() {

    const LoginSummit = async (e: any) => {
        e.preventDefault();
    }

    return (
        <div className=" w-[500px] bg-gray-300 shadow-lg p-[50px] rounded-xl mx-auto flex, flex-col">
            <h2 className="text-black text-[30px] font-bold text-center">Enter User and Password</h2>
            <div className=" flex flex-col">

                <form onSubmit={LoginSummit} className="flex flex-col">
                    <div className="flex mb-5">
                        <h4 className="w-[100px] text-white font-bold">User</h4>
                        <input type="text" className="bg-white rounded-md w-[300px] pl-2" />
                    </div>

                    <div className="flex">
                        <h4 className="w-[100px] text-white font-bold">Password</h4>
                        <input type="text" className="bg-white rounded-md w-[300px] pl-2" />
                    </div>

                    <button className="bg-gray-900 text-white rounded-md hover:bg-slate-500 mx-auto mt-5 font-bold p-2">Enter</button>

                </form>
            </div>
        </div>
    )
}