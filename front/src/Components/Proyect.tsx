export default function Proyect(props: any) {

    const { completed = 75 } = props;

    return (
        <div className=" flex flex-col border-2 border-white rounded-lg m-[10px]">
            <h3 className="font-bold text-gray-600 mx-auto mt-3 mb-[25px]">Proyect_Name</h3>

            <div className="flex mx-auto">
                <h3 className="text-gray-600 font-bold mr-[20px]">Progress</h3>
                <div className="h-[30px] w-[200px] bg-[#e0e0de] rounded-full">
                    <div className={`h-[100%] w-[${completed}%] bg-red-800 text-right rounded-full px-2`}>
                        <span className="p-[5] text-white font-bold">{`${completed}%`}</span>
                    </div>
                </div>


            </div>
            <button className="bg-slate-400 hover:bg-slate-600 rounded-lg h-{30px} w-[100px] mx-auto mt-[25px] mb-3">Edit</button>
        </div>
    )
}