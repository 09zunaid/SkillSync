import { motion } from 'framer-motion';

const Card = ({ children, className = '', delay = 0 }) => {
    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.9, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{
                duration: 0.4,
                delay: delay,
                type: 'spring',
                stiffness: 100
            }}
            className={`bg-white rounded-[2rem] border border-gray-100 shadow-sm hover:shadow-md transition-shadow duration-300 p-6 ${className}`}
        >
            {children}
        </motion.div>
    );
};

export default Card;
